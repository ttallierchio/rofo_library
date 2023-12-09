import { LitElement, html } from 'https://cdn.jsdelivr.net/gh/lit/dist@2/core/lit-core.min.js';;

export class listElement extends LitElement {
    static properties = {
        _listItems: { state: true },
    };

    constructor() {
        super()
        this._listItems = [1];
        this.grabData()

    }

    get input() {
        return this.renderRoot?.querySelector('#newitem') ?? null;
    }

    async grabData() {

        const response = await fetch(`/list_items`);
        const data = await response.json();
        console.log(data)
        this._listItems = data
        console.log(data[0])
        
    }
    async addItem() {
        const response = await fetch(`/write_new_item`,{
            method:"POST",
            headers: {
            "Content-Type": "application/json"}   ,
            body:JSON.stringify({"value":this.input.value})});

        const data = await response.json()
        this._listItems = [
            ...this._listItems,
            {desc:this.input.value,id:data.id}];

        console.log(this.input.value)
        this.input.value = '';
    }
    async delItem(id) {
        console.log(id);
        const response = await fetch(`/delete_item`,{
            method:"DELETE",
            headers: {
            "Content-Type": "application/json"}   ,
            body:JSON.stringify({"id":id})});
            await this.grabData();
    }
    render() {
        
        return html`
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <div class="container">
        <h2>all of the things!</h2>
        <ul class="list-group">
            ${this._listItems.map((item) =>
            html`
            <div class="row">
                <div class="col-sm">
                    <li class="w-auto list-group-item" id=${item.id}>${item.desc}</li>
                </div>
                <div class="col-sm">
                    <div class="btn-group mr-2" role="group" aria-label="First group">
                        <button type="button" class="btn btn-danger" @click=${() => this.delItem(item.id)}><img src="/static/trash-can.png"></button>
                        <button type="button" class="btn btn-primary" ><img src="/static/pencil(2).png"></button>
                    </div>
                </div>
            </div>
                    `
            )}
        </ul>
        <div class="row">
            <input id="newitem" aria-label="New item">
            <button class="btn btn-primary" @click=${this.addItem}>Add</button>
        </div>
    </div>        
  `;
    }
}
customElements.define('list-element', listElement);