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
  //private readonly apiUrl = 'http://localhost:8000/api/scraper';
  private readonly apiUrl =
    'https://smart-scraper-backend.purplestone-f82c5670.eastus.azurecontainerapps.io/api/scraper';

  constructor(private http: HttpClient) {}

  scrapeWebsite(url: string, type: string): Observable<ScrapeResponse> {
    switch (type) {
      case 'static':
        console.log('Using static scraper');
        return this.scrapeStatic(url);
      case 'dynamic':
        console.log('Using dynamic scraper');
        return this.scrapeDynamic(url);
      case 'api':
        console.log('Using API scraper');
        return this.scrapeApi(url);
      default:
        throw new Error(`Unknown scrape type: ${type}`);
    }
  }

  scrapeStatic(url: string): Observable<ScrapeResponse> {
    return this.http.post<ScrapeResponse>(`${this.apiUrl}/static`, { url });
  }

  scrapeDynamic(url: string): Observable<ScrapeResponse> {
    return this.http.post<ScrapeResponse>(`${this.apiUrl}/dynamic`, { url });
  }

  scrapeApi(url: string): Observable<ScrapeResponse> {
    var output = this.http.post<ScrapeResponse>(`${this.apiUrl}/api`, { url });
    console.log('API Scraper called: ', output);
    return output;
  }
}
