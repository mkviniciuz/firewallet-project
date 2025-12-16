const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("api", {
    login: (cpf, senha) => ipcRenderer.invoke("login-request", { cpf, senha }),
    navegar: (pagina) => ipcRenderer.send("carregar-pagina", pagina),
    buscarSaldo: (id) => ipcRenderer.invoke('get-saldo-python', id)
});
