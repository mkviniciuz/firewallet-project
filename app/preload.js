const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("api", {
    login: (cpf, senha) => ipcRenderer.invoke("login-request", { cpf, senha }),
    buscarSaldo: (cpf) => ipcRenderer.invoke('get-saldo-python', {cpf})
});
