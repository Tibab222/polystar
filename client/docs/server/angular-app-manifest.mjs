
export default {
  bootstrap: () => import('./main.server.mjs').then(m => m.default),
  inlineCriticalCss: true,
  baseHref: '/polystar/',
  locale: undefined,
  routes: [
  {
    "renderMode": 2,
    "route": "/polystar"
  },
  {
    "renderMode": 2,
    "redirectTo": "/polystar",
    "route": "/polystar/**"
  }
],
  entryPointToBrowserMapping: undefined,
  assets: {
    'index.csr.html': {size: 512, hash: '40042f41e6a14984f5ebb34095cd5ea50e1bd6ab663ea37a9c0c3e0392e9dafd', text: () => import('./assets-chunks/index_csr_html.mjs').then(m => m.default)},
    'index.server.html': {size: 1025, hash: '6a34a63e896d1c27547fb66aac080e74582001f23b5da3ec942ea5ef05984279', text: () => import('./assets-chunks/index_server_html.mjs').then(m => m.default)},
    'index.html': {size: 3714, hash: 'd50b84e3f43cb99c083f7e9010b0f9827a97881e59275dd69674c56849871244', text: () => import('./assets-chunks/index_html.mjs').then(m => m.default)},
    'styles-5INURTSO.css': {size: 0, hash: 'menYUTfbRu8', text: () => import('./assets-chunks/styles-5INURTSO_css.mjs').then(m => m.default)}
  },
};
