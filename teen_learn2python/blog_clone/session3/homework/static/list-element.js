import { LitElement, html } from 'https://cdn.jsdelivr.net/gh/lit/dist@2/core/lit-core.min.js';;

export class listElement extends LitElement {
    static properties = {
        _listItems: { state: true },
    };

    constructor() {
        super()
        this._listItems = ["item1", "item2"];
    }

    get input() {
        return this.renderRoot?.querySelector('#newitem') ?? null;
    }

    addItem() {
        this._listItems = [
            ...this._listItems,
            this.input.value];
        this.input.value = '';
    }

    delItem(val) {
        console.log(this._listItems)
        var new_array = [];
        this._listItems.forEach((value) => {
            if (value != val) {
                new_array = [...new_array, value];
            }
        }
        )
        console.log(new_array)
        this._listItems = [...new_array]
    }
    render() {
        return html`
    <h2>all of the things!</h2>
    <ul>
         ${this._listItems.map((item) =>
            html`<li>${item}<button @click=${() => this.delItem(item)}>DELETE</button></li>`
        )}
    </ul>
    <input id="newitem" aria-label="New item">
    <button @click=${this.addItem}>Add</button>
  `;
    }
}
customElements.define('list-element', listElement);