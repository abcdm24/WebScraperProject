import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class ScraperService {
  private readonly apiUrl = 'http://localhost:8000/scraper';

  constructor(private http: HttpClient) {}

  scrapeStatic(url: string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/static`, { url });
  }

  scrapeDynamic(url: string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/dynamic`, { url });
  }

  scrapeApi(url: string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/api`, { url });
  }
}
