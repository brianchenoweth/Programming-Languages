#include <stdio.h>
#include "lua.h"
#include "lualib.h"
#include "lauxlib.h"


int main (int argc,char*argv[])
{

	printf("Assignment #4-1, Brian Chenoweth, masc1367\n");
	
	lua_State *L = luaL_newstate();

	luaL_openlibs(L);
	
	luaL_dofile(L,argv[1]);

	lua_close(L);

	return 0;
}
