import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { of } from 'rxjs';

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
  private readonly API_URL = 'http://localhost:8000/api/history';

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
    return this.http.get<ScrapeHistory[]>(this.API_URL);
  }

  getById(id: string): Observable<ScrapeHistory> {
    return this.http.get<ScrapeHistory>(`${this.API_URL}/${id}`);
  }
}
