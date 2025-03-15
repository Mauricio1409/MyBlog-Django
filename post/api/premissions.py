from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permiso personalizado que solo permite a los administradores modificar el recurso,
    y permite acceso de solo lectura a todos los demás usuarios.
    """

    def has_permission(self, request, view):
        # Permite el acceso solo de lectura (GET, HEAD, OPTIONS) a todos los usuarios
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Solo los administradores pueden modificar (POST, PUT, PATCH, DELETE)
        return request.user and request.user.is_staff
    
    