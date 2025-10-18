import { Routes, RouterModule } from '@angular/router';

export const routes: Routes = [
  { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
  {
    path: 'dashboard',
    loadComponent: () => import('./features/dashboard/dashboard').then((m) => m.Dashboard),
  },
  {
    path: 'upload',
    loadChildren: () => import('./features/upload/upload-module').then((m) => m.UploadModule),
  },
  {
    path: 'history',
    loadChildren: () => import('./features/history/history-module').then((m) => m.HistoryModule),
  },
];
