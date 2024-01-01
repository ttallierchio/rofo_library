import { LitElement, html } from 'https://cdn.jsdelivr.net/gh/lit/dist@2/core/lit-core.min.js';;

export class isEven extends LitElement {
    static properties = {
        is_even: { state: true },
    };

    constructor() {
        super()
        this.is_even = "";

    }

    get input() {
        return this.renderRoot?.querySelector('#item') ?? null;
    }
    async grabData() {
        const response = await fetch(`/is_even/${this.input.value}`);


        const data = await response.json();
        console.log(data.value)
        if (data.value == "yes") {
            this.is_even = "Yes its even!"
        }
        else {
            this.is_even = "No it's Not"
        }
    }



    render() {
        return html`
    <h2>enter a number to see if its even!</h2>
    
    <input id="item" aria-label="Is it even?">
    <button @click=${this.grabData}>check value</button>
    ${this.is_even}
  `;
    }
}
customElements.define('is-even', isEven);