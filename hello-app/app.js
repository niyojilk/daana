const http = require('http');
const fs = require('fs');

const port = 3000;

const server = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(`
      <!DOCTYPE html>
      <html>
      <head>
        <title>Daana Hello World</title>
        <style>
          body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
          h1 { color: #4CAF50; }
        </style>
      </head>
      <body>
        <h1>Hello, World!</h1>
        <p>Welcome to the Daana App Server</p>
      </body>
      </html>
    `);
  } else {
    res.writeHead(404);
    res.end('Not Found');
  }
});

server.listen(port, () => {
  console.log(`Hello World server running at http://localhost:${port}`);
});
