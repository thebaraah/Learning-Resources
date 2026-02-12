import { apiReference } from '@scalar/express-api-reference';
import fs from 'fs';
import yaml from 'js-yaml';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const openApiSpec = yaml.load(
  fs.readFileSync(path.join(__dirname, 'openapi.yaml'), 'utf8')
);

export function setupApiDocs(app) {
  // Serve the raw OpenAPI spec as JSON
  app.get('/openapi.json', (_req, res) => {
    res.json(openApiSpec);
  });

  // Serve the Scalar API reference UI
  app.use(
    '/api-docs',
    apiReference({
      spec: {
        url: '/openapi.json',
      },
    })
  );
}
