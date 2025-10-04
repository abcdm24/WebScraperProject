import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { Routes, RouterModule } from '@angular/router';
import { UploadRoutingModule } from './upload-routing-module';
import { Upload } from './upload';
import { MatButton, MatButtonModule } from '@angular/material/button';

const routes: Routes = [{ path: '', component: Upload }];

@NgModule({
  declarations: [Upload],
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    UploadRoutingModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    RouterModule.forChild(routes),
  ],
})
export class UploadModule {}
