import { Component } from '@angular/core';
import {CancionesService} from './canciones.service'
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  providers: [CancionesService],
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Bienvenidos a TutorialCanciones';
  canciones = [];
  checkoutForm = this.formBuilder.group({
    titulo: ''
  });

constructor(private cancionesService: CancionesService, private formBuilder: FormBuilder) {}

  ngOnInit() {
    this.getCanciones("");
  }

  getCanciones(nombre): void {
    this.cancionesService.getCanciones(nombre)
      .subscribe(canciones => (this.canciones = canciones));
  }

  onSubmit(): void {
    // Process checkout data here
    this.getCanciones(this.checkoutForm.value.titulo);
  }
}
