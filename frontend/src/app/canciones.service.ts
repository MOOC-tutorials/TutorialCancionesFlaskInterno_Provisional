import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';


@Injectable()
export class CancionesService {

  constructor(private httpClient: HttpClient) { }

  public getCanciones(nombre : String): Observable<any>{
      var query : String =(nombre!="")?`?nombre=${nombre}`:"";
      return this.httpClient.get(`http://127.0.0.1:5000/canciones${query}`);
  }
}
