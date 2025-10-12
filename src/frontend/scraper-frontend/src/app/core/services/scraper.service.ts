import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

export interface ScrapeResult {
  url: string;
  metadata: any;
  headings: string[];
  links: string[];
  images: string[];
  text: string;
}

export interface ScrapeResponse {
  status: string;
  data?: ScrapeResult;
  error?: string;
}

@Injectable({ providedIn: 'root' })
export class ScraperService {
  private readonly apiUrl = 'http://localhost:8000/scraper';

  constructor(private http: HttpClient) {}

  scrapeStatic(url: string): Observable<ScrapeResponse> {
    return this.http.post<ScrapeResponse>(`${this.apiUrl}/static`, { url });
  }

  scrapeDynamic(url: string): Observable<ScrapeResponse> {
    return this.http.post<ScrapeResponse>(`${this.apiUrl}/dynamic`, { url });
  }

  scrapeApi(url: string): Observable<ScrapeResponse> {
    return this.http.post<ScrapeResponse>(`${this.apiUrl}/api`, { url });
  }
}
