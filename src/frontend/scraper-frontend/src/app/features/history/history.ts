import { Component, OnInit } from '@angular/core';
import { HistoryService, ScrapeHistory } from '../../core/services/history.service';
import { MatTableDataSource } from '@angular/material/table';

@Component({
  selector: 'app-history',
  standalone: false,
  templateUrl: './history.html',
  styleUrl: './history.scss',
})
export class History implements OnInit {
  history = new MatTableDataSource<ScrapeHistory>();
  displayedColumns: string[] = ['url', 'type', 'status', 'timestamp'];

  constructor(private historyService: HistoryService) {}

  ngOnInit(): void {
    this.historyService.getHistory().subscribe({
      next: (data) => (this.history.data = data),
      error: (err) => console.error('Failed to fetch history', err),
    });
  }
}
