
const electron = require('electron');

process.once('loaded', () => {
    // console.log('---- preload.js loaded ----');
    global.process = process;
    //global.module = module;
    global.electron = electron;
});