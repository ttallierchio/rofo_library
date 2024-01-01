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
        this._listItems = data

    }

    async addItem() {
        const response = await fetch(`/write_new_item`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ "value": this.input.value })
        });

        const data = await response.json()
        this._listItems = [
            ...this._listItems,
            { desc: this.input.value, id: data.id }];

        console.log(this.input.value)
        this.input.value = '';
    }

    async commitEdit(id) {
        const list_item_input = this.renderRoot?.querySelector(`#ip_${id}`) ?? null;

        alterEditItemState(id, false)
        const response = await fetch(`/update_item`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ "id": id, "value": list_item_input.value })
        })
        this.grabData()

    }



    async alterEditItemState(id, state) {
        const list_item_input = this.renderRoot?.querySelector(`#ip_${id}`) ?? null;
        const cancel_button = this.renderRoot?.querySelector(`#btn_cancel_${id}`) ?? null;
        const commit_button = this.renderRoot?.querySelector(`#btn_commit_${id}`) ?? null;
        const delete_button = this.renderRoot?.querySelector(`#btn_delete_${id}`) ?? null;
        const update_button = this.renderRoot?.querySelector(`#btn_update_${id}`) ?? null;
        const list_item = this.renderRoot?.querySelector(`#li_${id}`) ?? null;

        list_item_input.hidden = state;
        cancel_button.hidden = state;
        commit_button.hidden = state;
        delete_button.hidden = !state;
        update_button.hidden = !state;
        list_item.hidden = !state;

        return true;
    }

    async delItem(id) {
        const response = await fetch(`/delete_item`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ "id": id })
        });
        await this.grabData();
    }
    render() {

        return html`
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <div class="container">
        <h2>A List of Things!</h2>
        <ul class="list-group">
            ${this._listItems.map((item) =>
            html`
            <div class="row">
                <div class="col-sm">
                    <input id="ip_${item.id}" class="form-control" hidden=true value=${item.desc}>
                    <div class="btn-group mr-2" role="group" aria-label="First group">
                    <button type="button" id="btn_cancel_${item.id}" class="btn btn-danger" hidden=true @click=${() => this.alterEditItemState(item.id, true)}><img src="/static/x-mark.png"></button>
                    <button type="button" id="btn_commit_${item.id}" class="btn btn-primary" hidden=true @click=${() => this.commitEdit(item.id)}><img src="/static/tick-inside-circle.png"></button>
                </div>
                    <li class="w-auto list-group-item" id=li_${item.id}>${item.desc}
                     </li>
                </div>
                <div class="col-sm">
                    <div class="btn-group mr-2" role="group" aria-label="First group">
                        <button type="button" id="btn_delete_${item.id}" class="btn btn-danger" @click=${() => this.delItem(item.id)}><img src="/static/trash-can.png"></button>
                        <button type="button" id="btn_update_${item.id}" class="btn btn-primary" @click=${() => this.alterEditItemState(item.id, false)}><img src="/static/pencil.png"></button>
                    </div>
                </div>
            </div>
                    `
        )}
        </ul>
        <div class="row">
            <div>
                <input id="newitem" class="form-control" placeholder="New List Item" aria-label="New item">
            </div>
            <div>
                <button class="btn btn-primary" @click=${this.addItem}>Add</button>
            </div>
        </div>
    </div>        
  `;
    }
}
customElements.define('list-element', listElement);