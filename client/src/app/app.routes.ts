import { Routes } from '@angular/router';
import { TrajectoryComponent } from './components/trajectory/trajectory.component';

export const routes: Routes = [
  { path: '', component: TrajectoryComponent }, 
  { path: '**', redirectTo: '' }  
];
