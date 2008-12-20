Summary:	Additional file formats support for Tk
Summary(pl.UTF-8):	Obsługa dodatkowych formatów plików dla Tk
Name:		tk-Img
Version:	1.2.4
Release:	4
License:	distributable
Group:		Development/Languages/Tcl
Source0:	http://www.neosoft.com/tcl/ftparchive/sorted/packages-8.0/graphics/Img/1.2/img%{version}.tar.gz
# Source0-md5:	abfda1cc55555fc2490e761bde165078
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-jpeg.patch
Patch2:		%{name}-tk84.patch
Patch3:		%{name}-tk85.patch
URL:		http://tkimg.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel >= 3.5.5
BuildRequires:	tcl-devel
BuildRequires:	tk-devel >= 8.5.0
BuildRequires:	zlib-devel >= 1.1.3
Requires:	tk >= 8.4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package enhances Tk, adding support for many other Image formats:
BMP, XBM, XPM, GIF (with transparency, but without LZW), PNG, JPEG,
TIFF and PostScript.

%description -l pl.UTF-8
Ten pakiet rozszerza Tk, dodając obsługę wielu formatów graficznych:
BMP, XBM, XPM, GIF (z przezroczystością, ale bez LZW), PNG, JPEG, TIFF
oraz PostScript.

%prep
%setup -qn img%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make} \
	IMG_LD_SEARCH_FLAGS="" \
	CFLAGS="%{rpmcflags} -I/usr/include/tcl-private/generic -I/usr/include/tcl-private/unix"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	IMG_LD_SEARCH_FLAGS=""

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE README changes license.terms
%{_prefix}/lib/Img*
