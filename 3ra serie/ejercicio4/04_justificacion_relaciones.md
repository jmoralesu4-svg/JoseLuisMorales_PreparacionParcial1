# Justificación de las relaciones UML

## User - Ticket: solicitante

La relación es una asociación porque un usuario puede solicitar tickets
y tanto el usuario como el ticket mantienen su propia identidad.

La multiplicidad es:

User "1" -- "0..*" Ticket

Un usuario puede tener cero o muchos tickets.

## User - Ticket: técnico

También es una asociación porque el usuario puede existir aunque no tenga
tickets asignados.

La multiplicidad del técnico es:

User "0..1" -- "0..*" Ticket

Un ticket puede tener cero o un técnico asignado.

## Ticket - Comment

Es una composición porque los comentarios pertenecen al ticket.

La relación es:

Ticket "1" *-- "0..*" Comment

Un ticket puede tener cero o muchos comentarios.

El rombo negro está del lado de Ticket porque representa el todo.

## Ticket - History

Es una composición porque el historial forma parte del ticket.

La relación es:

Ticket "1" *-- "0..*" History

Un ticket puede tener cero o muchos registros de historial.

El rombo negro está del lado de Ticket.

## User - Article

Es una asociación porque un usuario puede crear artículos y el usuario
puede seguir existiendo aunque el artículo deje de existir.

La relación es:

User "1" -- "0..*" Article

Un usuario puede tener cero o muchos artículos.