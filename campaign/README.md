For the frontend:
 - in cPanel file manager go to public_html;
 - delete folder "static" and files `index.html`, `assets-manifest.json`, `archive.zip`
 - `npm run build` in `campaign/client`
 - zip the contents of the `build` directory
 - upload in `public_html`
 - unzip using file manager

For the backend:
 - in cPanel / software / setup python app
   - stop the current app
 - in cPanel / file manager
 - delete "server.jointrivial.com/backend"
 - zip `campaign/backend`
 - upload in "server.jointrivial.com"
 - unzip using file manager
 - in cPanel / software / setup python app
   - start the app
