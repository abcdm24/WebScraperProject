import { Component } from '@angular/core';
import { ScraperService } from '../../core/services/scraper.service';

@Component({
  selector: 'app-upload',
  standalone: false,
  templateUrl: './upload.html',
  styleUrl: './upload.scss',
})
export class Upload {
  url = '';
  output: any;

  constructor(private scraper: ScraperService) {}

  onScrapeStatic() {
    this.scraper.scrapeStatic(this.url).subscribe((res) => {
      this.output = res;
    });
  }
}
