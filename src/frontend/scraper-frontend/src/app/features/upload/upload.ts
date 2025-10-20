import { Component, ViewEncapsulation } from '@angular/core';
import { ScraperService } from '../../core/services/scraper.service';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-upload',
  standalone: false,
  templateUrl: './upload.html',
  styleUrl: './upload.scss',
  encapsulation: ViewEncapsulation.None,
})
export class Upload {
  url = '';
  scrapedData: any = null;
  loading = false;
  scrapeType: string = 'static';

  constructor(private scraper: ScraperService, private snackBar: MatSnackBar) {}

  onScrape(): void {
    // this.scraper.scrapeStatic(this.url).subscribe((res) => {
    //   this.output = res;
    // });
    if (!this.url) {
      this.snackBar.open('Please enter a valid URL', 'Close', { duration: 2000 });
      return;
    }

    this.loading = true;
    this.scraper.scrapeWebsite(this.url, this.scrapeType).subscribe({
      next: (res) => {
        if (res.status === 'success' && res.data) {
          console.log('Scraping successful:', res.data);
          this.scrapedData = res.data;
        } else {
          console.error('Scraping failed:', res.error);
        }
        this.loading = false;
      },
      error: (err) => {
        console.error('API error:', err);
        this.loading = false;
      },
    });
  }

  downloadJson(): void {
    const blob = new Blob([JSON.stringify(this.scrapedData, null, 2)], {
      type: 'application/json',
    });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'scraped_data.json';
    a.click();
  }
}
