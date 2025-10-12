import { Inject, Injectable } from '@angular/core';
import { OverlayContainer } from '@angular/cdk/overlay';

@Injectable({
  providedIn: 'root',
})
export class ThemeService {
  private darkClass = 'dark-mode';

  constructor(private overlay: OverlayContainer) {}

  enableDarkMode() {
    document.body.classList.add(this.darkClass);
    this.overlay.getContainerElement().classList.add(this.darkClass);
  }

  enableLightMode() {
    document.body.classList.remove(this.darkClass);
    this.overlay.getContainerElement().classList.remove(this.darkClass);
  }

  toggleMode(isDark: boolean) {
    //alert(isDark);
    if (isDark) {
      this.enableDarkMode();
    } else {
      this.enableLightMode();
    }
  }

  isDarkMode(): boolean {
    return document.body.classList.contains(this.darkClass);
  }
}
