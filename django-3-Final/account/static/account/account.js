export class AccountComponent extends HTMLElement{
	constructor(){
		super()
		this.attachShadow({mode: "open"})
		this.shadowRoot.innerHTML=this.template()
		this.navLinkHandler = this.navLinkHandler.bind(this)
		this.navBarBrandHandler = this.navBarBrandHandler.bind(this)
		this.title = `${this.dataset.username} ${document.title}`
	}

	template(){
		return `
			<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
			<div class="vh-100">
				<nav class="navbar navbar-light bg-light">
					<div class="container-fluid">
						<a class="navbar-brand" href="#">Logged as ${this.dataset.username}</a>	
						<a class="nav-link" href="#" data-channel="channel_1">Channel_1</a>
						<a class="nav-link" href="#" data-channel="channel_2">Channel_2</a>
						<a class="nav-link" href="#" data-channel="channel_3">Channel_3</a>
						<button class="btn btn-outline-success" type="button" id="logoutBtn">Logout</button>
					</div>
				</nav>
				<div id="chatroom" class="container h-100 pb-5" ></div>
				<footer class="container-fluid position-absolute bottom-0 bg-light text-center">pnamnil@42Bangkok</footer>
			</div>
		`
	}

	logout(){
			const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]')
			fetch(`${window.location.origin}/logout/`, {
					method: 'POST',
					headers: {
						"X-CSRFToken": csrf_token.value,
					}
			})
			.then(response => response.json())
			.then(data => {
				if (data.success) {
					csrf_token.value = data.csrf_token
					document.cookie = `csrftoken=${data.csrf_token}; path=/;`;
					document.getElementById("main").innerHTML='<connect-component></connect-component>'
				} else {
					// this.shadowRoot.getElementById('errorList').innerText = data.errors.invalid_login
				}
			})
	}

	navLinkHandler(event){
		event.preventDefault()
		const active = this.shadowRoot.querySelector('a.text-primary')
		const chatComponent = `<chat-component data-channel=${event.target.dataset.channel} data-username=${this.dataset.username}></chat-component>`
		if (!active) {
			event.target.classList.add('text-primary')
			this.shadowRoot.getElementById("chatroom").innerHTML=chatComponent
		}
		else if (event.target != active) {
			active.classList.remove('text-primary')
			event.target.classList.add('text-primary')
			this.shadowRoot.getElementById("chatroom").innerHTML=chatComponent
		}
	}

	navBarBrandHandler(event){
		event.preventDefault()
		document.title = this.title
		this.shadowRoot.getElementById("chatroom").innerHTML = ""
	}

	connectedCallback(){
		this.shadowRoot.getElementById("logoutBtn").addEventListener('click', this.logout)
		const navLinks = this.shadowRoot.querySelectorAll('a.nav-link')
		for (const navLink of navLinks){
			navLink.addEventListener('click', this.navLinkHandler)
		}

		this.shadowRoot.querySelector('a.navbar-brand').addEventListener('click', this.navBarBrandHandler)

		/** set title */
		document.title = this.title

		//debug
		this.shadowRoot.querySelector("[data-channel=channel_2]").click()
	}
}
