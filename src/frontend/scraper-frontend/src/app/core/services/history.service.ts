import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { of } from 'rxjs';
import { environment } from '../../../environments/environment';

export interface ScrapeHistory {
  id: string;
  url: string;
  type: 'static' | 'dynamic' | 'api';
  status: 'success' | 'error';
  timestamp: string;
  data?: any;
}

@Injectable({
  providedIn: 'root',
})
export class HistoryService {
  // private readonly API_URL = 'http://localhost:8000/api/history';
  private readonly API_URL = environment.apiUrl + 'history';
  //  'https://smart-scraper-backend.purplestone-f82c5670.eastus.azurecontainerapps.io/api/history';

  constructor(private http: HttpClient) {}

  getHistory(): Observable<ScrapeHistory[]> {
    //return this.http.get<ScrapeHistory[]>(this.API_URL);
    // return of([
    //   {
    //     id: '1',
    //     url: 'https://example.com',
    //     type: 'static',
    //     status: 'success',
    //     timestamp: new Date().toISOString(),
    //   },
    //   {
    //     id: '2',
    //     url: 'https://news.ycombinator.com',
    //     type: 'dynamic',
    //     status: 'error',
    //     timestamp: new Date().toISOString(),
    //   },
    // ]);
    console.log('Fetching history from API:', this.API_URL);
    return this.http.get<ScrapeHistory[]>(this.API_URL);
  }

  getById(id: string): Observable<ScrapeHistory> {
    return this.http.get<ScrapeHistory>(`${this.API_URL}/${id}`);
  }
}
