import { LitElement, html } from 'https://cdn.jsdelivr.net/gh/lit/dist@2/core/lit-core.min.js';;

export class carInfo extends LitElement {
    static properties = {
        data: { state: true },
    };
    constructor() {
        super()
        this.data = {"make":"ford","model":"escort","year":2023,"color":"Red"};
    }


    async grabData() {
        const response = await fetch(`/car`);
        const data = await response.json();
        console.log(this.data)
        this.data = data
        
        console.log(data)
        console.log(this.data)
    }

    render() {
        return html`
    <p> <div><div>
      ${this.data.make}<br>
      ${this.data.model}<br>
      ${this.data.year}<br>
      ${this.data.color}<br>
      </div>
      <div>
      <button @click=${this.grabData}>go forth and get other car data</button>
      </div>
     </div>
    </p>`;
    }
}

customElements.define('car-info', carInfo);