{
    const ipc = window.electron.ipcRenderer;

    ipc.on('async-reply', (event: any, arg: any) => {
        console.log(arg);
    });
    ipc.send('async', 'ping');
}