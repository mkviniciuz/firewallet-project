const { app, BrowserWindow, ipcMain} = require("electron");
const { spawn } = require("child_process");
let pyProc;
const path = require("path");

function createWindow() {
  const win = new BrowserWindow({
    width: 393,
    height: 852,
    frame: false,
    resizable: false,
    icon: path.join(__dirname, 'front-end/assets/img/app-icon.png'),
    webPreferences: {
      contextIsolation: true,
      preload: path.join(__dirname, "preload.js")
    }
  });

  win.loadFile("front-end/index.html");
}

app.whenReady().then(() => {
  // Inicia o backend Python
    pyProc = spawn("python", ["../backend/main.py"]);

    pyProc.stdout.on("data", (data) => {
        console.log("PYTHON:", data.toString());
    });

    pyProc.stderr.on("data", (data) => {
        console.error("PYTHON ERROR:", data.toString());
    });

    // recebe pedidos do Electron (renderer)
    ipcMain.handle("login-request", async (event, { cpf, senha }) => {
        return new Promise((resolve) => {
            pyProc.stdin.write(JSON.stringify({ type: "login", cpf, senha }) + "\n");

            pyProc.stdout.once("data", (data) => {
                const resposta = JSON.parse(data.toString());
                resolve(resposta);
            });
        });
    });

    ipcMain.on("carregar-pagina", (event, pagina) => {
    const win = BrowserWindow.getFocusedWindow();
    win.loadFile(`front-end/${pagina}`);
});


  createWindow();

  app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") app.quit();
});
