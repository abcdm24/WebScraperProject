import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { History } from './history';

const routes: Routes = [{ path: '', component: History }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class HistoryRoutingModule {}
