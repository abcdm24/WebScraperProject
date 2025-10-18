import { Component } from '@angular/core';
import { MatCardModule } from '@angular/material/card';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [MatCardModule],
  template: `
    <div class="dashboard">
      <mat-card class="welcome-card">
        <h2>Welcome to Smart Scraper Dashboard</h2>
        <p>Here you'll soon see quick stats and summaries - for example:</p>
        <ul>
          <li>Total scraped performed</li>
          <li>Recent history items</li>
          <li>Average scrape duration</li>
        </ul>
      </mat-card>
    </div>
  `,
  styles: [
    `
      .dashboard {
        display: flex;
        justify-content: center;
        padding: 2rem;
      }
      .welcome-card {
        max-width: 600px;
        text-align: center;
      }
    `,
  ],
})
export class Dashboard {}
