export class ChatComponent extends HTMLElement{
	constructor(){
		super()
		this.attachShadow({mode: "open"})
		this.shadowRoot.innerHTML = this.template()
		this.socket = null
		this.chatMessages = this.shadowRoot.getElementById("chatMessages")
		this.inputMessage = this.shadowRoot.getElementById("inputMessage")
		this.userList = this.shadowRoot.getElementById("userList")
		this.sendForm = this.shadowRoot.getElementById("sendForm")
		this.sendMessage = this.sendMessage.bind(this)
		this.receiveMassage = this.receiveMassage.bind(this)
		this.handlePageRefresh = this.handlePageRefresh.bind(this);
	}

	template(){
		return `
			<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
			<style>
				.h-sm-75 {
					height: 100%;
				}
				.h-sm-25 {
					height: 100%;
				}
				@media (max-width: 575.98px) {
					.h-sm-75 {
						height: 75%;
					}
					.h-sm-25 {
						height: 25%;
					}					
				}
			</style>
			<div class="row h-100 p-3 pb-5">
				<!-- Chat Box -->
				<div class="col-sm-8 h-sm-75 d-flex flex-column mb-3">
					<!-- Chat Messages -->	
					<div class="border border-info rounded-2 flex-grow-1 d-flex flex-column justify-content-end overflow-hidden mb-2 px-2">
						<div id="chatMessages" class="w-100 overflow-auto pt-2">
							<!--div>User1: Hello!</div>
							<div>User2: Hi!</div-->
						</div>
					</div>

					<!-- Input Form (stays at the bottom) -->
					<div class="position-relative w-100">
						<form id="sendForm" class="d-flex gap-2">
							<input id="inputMessage" type="text" class="form-control" placeholder="Type your message..." required>
							<button type="submit" class="btn btn-primary">Send</button>
						</form>
					</div>
				</div>

				<!-- for show list of user -->
				<div class="h-sm-25 col-sm-4 px-2">
				<div id="userList" class="h-100 p-2 border border-danger d-flex flex-column rounded-2 overflow-auto"></div>
				</div>
			</div>
		`
	}

	scrollToBottom = () => {
		const container = this.shadowRoot.getElementById('chatMessages')
		container.scrollTop = container.scrollHeight
	}

	sendMessage(event){
		event.preventDefault()
		this.socket.send(JSON.stringify({body: this.inputMessage.value}))
		this.inputMessage.value = ""
	}

	/** handle message */
	messageGroup(obj){
		const div = document.createElement('div')
		if (obj.author == this.dataset.username){
			div.classList.add('text-end')
		}
		
		const p = document.createElement('p')
		p.innerText = obj.body

		const message = `
			<p class="d-inline border border-info rounded-top ${obj.author == this.dataset.username ? 'rounded-start' : 'rounded-end'} py-1 px-2">${obj.body}</p>
			<br>
			<span style="font-size: 0.6em;" class="fst-italic">@${obj.author}</span>
		`
		div.innerHTML = message

		return div
	}

	userGroup(user){
		const el = document.createElement('div')
		el.id = user
		el.innerHTML= `<p class=${this.dataset.username == user ? "text-info": ""}>${user}</p>`
		return el
	}

	connectionGroup(obj){
		const el = document.createElement('div')
		el.classList.add("text-center", obj.type == "new_connection" ? "text-info" : "text-danger")
		el.innerHTML= `<p>${obj.user} has ${obj.type == "new_connection" ? "join" : "left"} the chat</p>`
		return el 
	}
	/** */
	
	receiveMassage(event){
		const obj = JSON.parse(event.data)
		// console.log(obj)

		if (obj.type == 'connect') {
			for (const message of obj.messages.reverse()){
				this.chatMessages.appendChild(this.messageGroup(message))
			}
			for (const user of obj.users) {
				this.userList.appendChild(this.userGroup(user))
			}
		}
		else if (obj.type == 'new_connection' && obj.user != this.dataset.username) {
			const user = this.userList.querySelector(`#${obj.user}`)
			// console.log(user)
			if (user) return
			this.userList.appendChild(this.userGroup(obj.user))
			this.chatMessages.appendChild(this.connectionGroup(obj))
		}
		else if (obj.type == 'disconnection' && obj.user != this.dataset.username) {
			const user = this.userList.querySelector(`#${obj.user}`)
			user.remove()
			this.chatMessages.appendChild(this.connectionGroup(obj))
		}
		else if (obj.type == 'message_handler'){
			this.chatMessages.appendChild(this.messageGroup(obj))
		}
		this.scrollToBottom()
	}

	setupWebsocket(){
		this.socket = new WebSocket(`${window.location.origin}/ws/chatroom/${this.dataset.channel}`)
		// this.socket.addEventListener('open', function(){
		// 	console.log("webSocket connected")
		// })
		this.socket.addEventListener('message', this.receiveMassage)
		// this.socket.addEventListener('error', function(error){
		// 	console.log(`webSocket error ${typeof(error)}`)
		// })
		// this.socket.addEventListener('close', function(){
		// 	console.log("webSocket closed")
		// })
	}

	connectedCallback(){
		// console.log(`${this.dataset.channel} connected`)
		this.setupWebsocket()
		this.sendForm.addEventListener('submit', this.sendMessage)
        window.addEventListener('beforeunload', this.handlePageRefresh);
		document.title = `${this.dataset.username} on ${this.dataset.channel}`
	}

	cleanupWebSocket(){
		if (this.socket){
			this.socket.close()
			this.socket = null
		}
	}

	disconnectedCallback(){
		this.cleanupWebSocket()
        window.removeEventListener('beforeunload', this.handlePageRefresh);
	}

	handlePageRefresh(event) {
        // console.log('Page is about to be refreshed or closed');
        this.cleanupWebSocket();
    }
}
