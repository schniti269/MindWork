if (fork() != 0) /* parent code */
waitpid (-1, &status, 0);
else /* child code */
execve (command, parameters, 0);
}Wie funktioniert das?

   Tags & Topics:
   