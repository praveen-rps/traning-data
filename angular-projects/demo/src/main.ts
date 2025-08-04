import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { App } from './app/app';
import { Login } from './app/login/login';
import { Register } from './app/register/register';

bootstrapApplication(App, appConfig)
  .catch((err) => console.error(err));
