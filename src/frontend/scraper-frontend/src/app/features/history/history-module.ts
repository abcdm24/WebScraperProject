import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { Routes, RouterModule } from '@angular/router';
import { HistoryRoutingModule } from './history-routing-module';
import { History } from './history';
import { MatButton, MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatExpansionModule } from '@angular/material/expansion';
import { NgxJsonViewerModule } from 'ngx-json-viewer';
import { MatTableModule } from '@angular/material/table';

const routes: Routes = [{ path: '', component: History }];

@NgModule({
  declarations: [History],

  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    HistoryRoutingModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatIconModule,
    MatProgressSpinnerModule,
    MatExpansionModule,
    MatTableModule,
    RouterModule.forChild(routes),
    NgxJsonViewerModule,
  ],
})
export class HistoryModule {}
