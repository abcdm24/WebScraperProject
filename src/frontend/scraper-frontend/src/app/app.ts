import { Component, signal, Renderer2, OnInit } from '@angular/core';
import { RouterOutlet, RouterLink, RouterLinkActive, Router } from '@angular/router';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatTooltipModule } from '@angular/material/tooltip';
import { ThemeService } from './core/services/theme.service';
import { MatSlideToggle, MatSlideToggleModule } from '@angular/material/slide-toggle';
import { MaterialModule } from './shared/material/material.module';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    RouterLink,
    RouterLinkActive,
    MatIconModule,
    MatButtonModule,
    MatToolbarModule,
    MatTooltipModule,
    MatSlideToggleModule,
    MaterialModule,
  ],
  templateUrl: './app.html',
  styleUrl: './app.scss',
})
export class App implements OnInit {
  //isDark = signal(false);
  isDark = false;
  //constructor(private renderer: Renderer2) {}
  constructor(private themeSrv: ThemeService) {}

  ngOnInit() {
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    //this.isDark.set(prefersDark);
    //this.isDark = prefersDark;
    this.isDark = this.themeSrv.isDarkMode();
    //alert(this.isDark ? 'Dark mode' : 'Light mode');
    //this.updateTheme();

    //this.renderer.addClass(document.body, 'mat-typography');
  }

  // toggleTheme(checked: boolean) {
  //   this.isDark = checked;
  //   this.themeSrv.toggleMode(this.isDark);
  //   alert(this.isDark ? 'Dark mode' : 'Light mode');
  // }

  toggleTheme() {
    //this.isDark.set(!this.isDark());
    this.isDark = !this.isDark;
    //this.updateTheme();
    this.themeSrv.toggleMode(this.isDark);
  }

  // updateTheme() {
  //   if (this.isDark) {
  //     this.renderer.addClass(document.body, 'dark-theme');
  //   } else {
  //     this.renderer.removeClass(document.body, 'dark-theme');
  //   }
  // }

  protected readonly title = signal('Smart Scraper');
}
