import astropy.units as u

__all__ = ["M2MM", "R2ARCSEC", "MM2M", "ARCSEC2R"]

M2MM = u.m.to(u.mm)
R2ARCSEC = u.rad.to(u.arcsec)

MM2M = 1 / M2MM
ARCSEC2R = 1 / R2ARCSEC
