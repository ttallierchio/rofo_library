import { LitElement, html } from 'https://cdn.jsdelivr.net/gh/lit/dist@2/core/lit-core.min.js';;

export class dynamicElement extends LitElement {
    static properties = {
        random_number: { state: true },
    };
    constructor() {
        super()
        this.random_number = 0;
    }
    get input() {

        return this.renderRoot?.querySelector('#what_num') ?? 1;

    }

    async grabData() {
        const response = await fetch(`/random`);
        const data = await response.json();
        this.random_number = data.value
        console.log(data.value)
    }

    render() {
        return html`
    <p> <div><div>
      ${this.random_number}
      </div>
      <div>
      <button @click=${this.grabData}>go forth and get a random number</button>
      </div>
     </div>
    </p>`;
    }
}

customElements.define('dynamic-element', dynamicElement);