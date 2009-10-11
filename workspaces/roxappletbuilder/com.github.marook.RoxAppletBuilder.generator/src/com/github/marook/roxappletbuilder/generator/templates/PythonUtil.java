/*
 * Copyright 2009 Markus Pielmeier
 *
 * This file is part of rox applet builder.
 *
 * rox applet builder is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * rox applet builder is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with rox applet builder.  If not, see <http://www.gnu.org/licenses/>.
 */

package com.github.marook.roxappletbuilder.generator.templates;

import java.util.ArrayList;
import java.util.List;

public final class PythonUtil {
	
	private PythonUtil(){
		throw new IllegalStateException();
	}
	
    public static String getUID(final Object o){
        final int uid = System.identityHashCode(o);
        
        return Integer.toHexString(uid);
    }

    public static String multiply(final String s, final Long factor){
		final int factorInt = factor.intValue();
		
		if(factor == 0) return "";
		if(factor == 1) return s;
		
		final StringBuilder sb = new StringBuilder(s.length() * factorInt);
		for(int i = 0; i < factorInt; ++i){
			sb.append(s);
		}
		
		return sb.toString();
	}
    
    public static List<String> getPackages(final String p){
    	final String[] packageNames = p.split("[.]");
    	
    	final List<String> subPackages =
    		new ArrayList<String>(packageNames.length + 1);
    	subPackages.add("");
    	
    	final StringBuilder sb = new StringBuilder(p.length());
    	for(int i = 0; i < packageNames.length; ++i){
    		if(i > 0){
    			sb.append(".");
    		}
    		
    		sb.append(packageNames[i]);
    		
    		subPackages.add(sb.toString());
    	}
    	
    	return subPackages;
    }

}
