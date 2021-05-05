/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { CancionesService } from './canciones.service';

describe('CancionesService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [CancionesService]
    });
  });

  it('should ...', inject([CancionesService], (service: CancionesService) => {
    expect(service).toBeTruthy();
  }));
});
