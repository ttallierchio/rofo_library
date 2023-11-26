import { LitElement, html } from 'https://cdn.jsdelivr.net/gh/lit/dist@2/core/lit-core.min.js';

export class basicElement extends LitElement {


  render() {
    return html`
      <p> 
        I am your first component. 
        I am just a straight html render. 
        anything between these two tick marks becomes html.
      </p>`;
  }
}
customElements.define('basic-element', basicElement);
