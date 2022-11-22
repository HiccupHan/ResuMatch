if (typeof init == 'undefined') {
    const host = document.createElement('div');
    host.className = 'shadow-host';
    function init() {
        document.body.prepend(host);

        var shadowRoot = document.querySelector('.shadow-host').attachShadow({ mode: 'open' });

        const injectedElement = document.createElement('div');
        injectedElement.className = ('upload-container');
        injectedElement.innerHTML = `
        <style>
        .upload-container{
            position: fixed;
            width: 100vw;
            height: 100vh;
            background-color: rgba(129,129,129,0.6);
            z-index: 1000;
            display: flex;
            justify-content: center;
            align-items: center;}
        </style>
        <div className='upload-window' 
        style='width: 50vw; 
            height: 60vh; 
            border-style: solid;
            border-width: 2px;
            border-color: black;
            border-radius: 4px; 
            background-color: black;
            display: grid;
            grid-template-columns: 1fr 6fr 1fr;'>
        <button className='close-btn'
        style= 'justify-self: right; 
            height: 30px;
            width: 30px;
            text-align: center;
            box-sizing: border-box;
            grid-column-start: 3;'> X </button>
        <div className='upload-box' 
        style= 'background-color: white;
            margin: 0;
            padding: 0;
            border-style: dotted;
            border-color: black;
            border-radius: 4px;
            justify-self: center;
            align-self: center;
            grid-column-start: 2;
            grid-row-start: 1;
            width: 100%;
            height: 80%;'>
        upload your pdf</div>
        </div>`;
        shadowRoot.appendChild(injectedElement);
    }

    chrome.runtime.onMessage.addListener((request) => {
        if (request.type === 'open-modal') {
            init();
        }
    });

    chrome.runtime.onMessage.addListener((request) => {
        if (request.type === 'close-modal') {
            document.body.removeChild(host);
        }
    }); 
}


