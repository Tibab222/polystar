import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { TrajectoryService } from '../../services/trajectory.service';

@Component({
  selector: 'app-trajectory',
  standalone: true,
  templateUrl: './trajectory.component.html',
  styleUrls: ['./trajectory.component.scss'],
  imports: [FormsModule, CommonModule]
})
export class TrajectoryComponent {
  planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];
  origin: string = this.planets[0];
  destination: string = this.planets[1];
  data: any = null;
  loading: boolean = false;
  error: string = '';
  stepsToShow: any[] = [];
  private allSteps: any[] = [];

  constructor(private trajectoryService: TrajectoryService) {
    this.trajectoryService.getTrajectoryObservable().subscribe(response => {
      if (response?.error) {
        this.error = response.error;
        this.data = null;
      } else {
        this.data = response;
        this.error = '';
        this.stepsToShow = [];
        this.allSteps = response.steps;
        this.animateSteps();
      }
      this.loading = false;
    });
  }

  fetchTrajectory() {
    if (!this.origin || !this.destination) {
      this.error = 'Veuillez sélectionner deux planètes.';
      return;
    }

    this.loading = true;
    this.error = '';
    this.data = null;
    this.trajectoryService.getTrajectory(this.origin, this.destination);
  }

  animateSteps() {
    let index = 0;
    const interval = setInterval(() => {
      if (index < this.allSteps.length) {
        this.stepsToShow.push(this.allSteps[index]);
        index++;
      } else {
        clearInterval(interval);
      }
    }, 1000); // 🔥 Ajoute une étape toutes les 1 seconde
  }
}
