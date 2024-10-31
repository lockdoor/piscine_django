export class ConnectComponent extends HTMLElement{
	constructor(){
		super()
		this.attachShadow({mode: "open"})
		this.shadowRoot.innerHTML=this.template()
		this.connect = this.connect.bind(this)
	}

	template(){
		return `
		  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
		  <div class="vh-100 d-flex align-items-center justify-content-center">
			<!--p>Connect Component</p-->
			<form id="connectForm" class="w-75">
				<p  class="fs-1">Connect to Chatroom</p>
				${document.querySelector('[name=csrfmiddlewaretoken]').outerHTML}
				<div class="mb-3">
					<label for="usernameInput" class="form-label">Username: </label>
					<input type="text" name="username" id="usernameInput" class="form-control" required>
				</div>
				<div class="mb-3">
					<label for="passwordInput" class="form-label">Password: </label>
					<input type="password" name="password" id="passwordInput" class="form-control" required>
				</div>
				<input type="submit" value="connect" role="button" class="btn btn-primary" >
				<p id="errorList" class="text-danger"></p>
				
			</form>
		  </div>
		`
	}

	connect(event){
		event.preventDefault()
		const formData = new FormData(this.shadowRoot.getElementById("connectForm"))		
		const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]')

		fetch(`${window.location.origin}/connect/`, {
			method: "POST",
			body: formData,
			headers: {
				"X-CSRFToken": csrf_token.value,
			}
		})
		.then(response => response.json())
		.then(data => {
			if (data.success) {
				csrf_token.value = data.csrf_token
				document.cookie = `csrftoken=${data.csrf_token}; path=/;`;
				document.getElementById("main").innerHTML=`<account-component data-username='${data.username}'></account-component>`
			} else {
				this.shadowRoot.getElementById('errorList').innerText = data.errors.invalid_login
			}
		})
	}

	connectedCallback(){
		// console.log("hello")
		this.shadowRoot.getElementById("connectForm").addEventListener("submit", this.connect)
	}

}