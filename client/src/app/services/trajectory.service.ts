import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { catchError } from 'rxjs';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TrajectoryService {
  private apiUrl = 'https://ec2-3-98-57-130.ca-central-1.compute.amazonaws.com:8000/calcul';
  private trajectoryData = new BehaviorSubject<any>(null); 

  constructor(private http: HttpClient) {}

  getTrajectory(origin: string, destination: string) {
    this.http.get(`${this.apiUrl}/${origin}/${destination}`).pipe(
      catchError(err => {
        this.trajectoryData.next({ error: 'Erreur lors de la récupération des données.' });
        throw err;
      })
    ).subscribe(response => this.trajectoryData.next(response)); 
  }

  getTrajectoryObservable() {
    return this.trajectoryData.asObservable(); 
  }
}
