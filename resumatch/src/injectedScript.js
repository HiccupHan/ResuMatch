//note: scripts cannot be inserted in an html tag since it breaks security policies for many websites
//reference this page: https://stackoverflow.com/questions/9515704/access-variables-and-functions-defined-in-page-context-using-a-content-script

//if prevent multiple injects on page refresh
if (typeof init == 'undefined') {
    function init() {
        const host = document.createElement('div');
        host.className = 'shadow-host';
        document.body.prepend(host);

        //creates shadow root
        //note: to access shadow root inner elements, do document.querySelector('.shadow-host').shadowRoot then query the element name
        var shadowRoot = document.querySelector('.shadow-host').attachShadow({ mode: 'open' });

        const injectedElement = document.createElement('div');
        injectedElement.className = 'upload-container';
        injectedElement.style.position = 'fixed';
        injectedElement.style.width = '100vw';
        injectedElement.style.height = '100vh';
        injectedElement.style.backgroundColor = 'rgba(129,129,129,0.6)';
        injectedElement.style.zIndex = '1000';
        injectedElement.style.display = 'none';
        injectedElement.style.justifyContent = 'center';
        injectedElement.style.alignItems = 'center';

        const uploadWindow = document.createElement('div');
        uploadWindow.className = 'upload-window';
        uploadWindow.style.width = '50vw';
        uploadWindow.style.height = '60vh';
        uploadWindow.style.borderStyle = 'solid';
        uploadWindow.style.borderWidth = '2px';
        uploadWindow.style.borderColor = 'black';
        uploadWindow.style.borderRadius = '4px';
        uploadWindow.style.backgroundColor = 'black';
        uploadWindow.style.display = 'grid';
        uploadWindow.style.gridTemplateColumns = '1fr 6fr 1fr';

        const closeBtn = document.createElement('button');
        closeBtn.className = 'close-btn';
        closeBtn.style.height = '30px';
        closeBtn.style.width = '30px';
        closeBtn.style.textAlign = 'center';
        closeBtn.style.boxSizing = 'border-box';
        closeBtn.style.gridColumnStart = '3';
        closeBtn.style.justifySelf = 'right';
        closeBtn.innerHTML = 'X';

        const uploadBox = document.createElement('div');
        uploadBox.className = 'upload-box';
        uploadBox.style.width = '100%'
        uploadBox.style.height = '80%'
        uploadBox.style.borderStyle = 'dotted';
        uploadBox.style.borderColor = 'black';
        uploadBox.style.backgroundColor = 'white';
        uploadBox.style.borderRadius = '4px';
        uploadBox.style.justifySelf = 'center';
        uploadBox.style.alignSelf = 'center';
        uploadBox.style.gridColumnStart = '2';
        uploadBox.style.gridRowStart = '1';
        uploadBox.style.textAlign = 'center';
        uploadBox.innerHTML = 'Upload your PDF'

        uploadWindow.appendChild(closeBtn);
        uploadWindow.appendChild(uploadBox);
        injectedElement.appendChild(uploadWindow);
        shadowRoot.appendChild(injectedElement);
    }
    init();

    //assign click event listener to the close button in the popup menu and allow it to close the pop up menu
    function closeWindow() {
        const theButton = document.querySelector('.shadow-host').shadowRoot.querySelector('.close-btn');
        theButton.addEventListener('click', function () {
            const uploadModal = document.querySelector('.shadow-host').shadowRoot.querySelector('.upload-container');
            uploadModal.style.display = 'none';
        });
    }
    closeWindow();

    //open and close modal on chrome message
    chrome.runtime.onMessage.addListener((request) => {
        if (request.type === 'open-modal') {
            const uploadModal = document.querySelector('.shadow-host').shadowRoot.querySelector('.upload-container');
            uploadModal.style.display = 'flex';
        }
    });

    chrome.runtime.onMessage.addListener((request) => {
        if (request.type === 'close-modal') {
            const uploadModal = document.querySelector('.shadow-host').shadowRoot.querySelector('.upload-container');
            uploadModal.style.display = 'none';
        }
    });


}


