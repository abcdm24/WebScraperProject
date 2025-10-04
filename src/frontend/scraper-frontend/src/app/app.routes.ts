import { Routes, RouterModule } from '@angular/router';

export const routes: Routes = [
  { path: '', redirectTo: 'upload', pathMatch: 'full' },
  {
    path: 'upload',
    loadChildren: () => import('./features/upload/upload-module').then((m) => m.UploadModule),
  },
];
