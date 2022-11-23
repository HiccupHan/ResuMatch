import React from 'react';
import {render} from 'react-dom'

import PdfUpload from '../components/PdfUpload.js'

const pdfUpload = document.getElementById('pdf-upload');
if (pdfUpload !== null){
    render(<PdfUpload />, pdfUpload);
}

