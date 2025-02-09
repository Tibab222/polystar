import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';
import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),  // 🔥 Fournit la gestion des routes
    provideHttpClient()     // 🔥 Fournit le client HTTP pour appeler l'API
  ]
};
