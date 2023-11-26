import { LitElement, html } from 'https://cdn.jsdelivr.net/gh/lit/dist@2/core/lit-core.min.js';

export class repeatElement extends LitElement {
    static properties = {
        repeat_text: {},
    };

    constructor() {
        super();
        this.repeat_text = 'Echo, Echo, Echo';
    }

    changeText(event) {

        const input = event.target;

        this.repeat_text = input.value;

    }
    render() {
        return html`
      <p> <div><div>
        Echoing, your input box (${this.repeat_text})</div>
        <div>
       <input @input=${this.changeText}  placeholder="Echo whatever is typed here">
       </div>
      </p>`;
    }
}
customElements.define('repeat-element', repeatElement);
