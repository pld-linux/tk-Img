Summary:	Additional file formats support for Tk
Summary(pl):	Obs³uga dodatkowych formatów plików dla Tk
Name:		tk-Img
Version:	1.2.4
Release:	1
License:	distributable
Group:		Development/Languages/Tcl
Source0:	http://ftp.neosoft.com/cl/sorted/packages-8.0/graphics/%{name}/%{version}/img%{version}.tar.gz
# Source0-md5:	abfda1cc55555fc2490e761bde165078
Patch0:		%{name}-DESTDIR.patch
URL:		http://members1.chello.nl/~j.nijtmans/img.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel >= 3.5.5
BuildRequires:	tk-devel
BuildRequires:	zlib-devel >= 1.1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package enhances Tk, adding support for many other Image formats:
BMP, XBM, XPM, GIF (with transparency, but without LZW), PNG, JPEG,
TIFF and PostScript.

%description -l pl
Ten pakiet rozszerza Tk, dodaj±c obs³ugê wielu formatów graficznych:
BMP, XBM, XPM, GIF (z przezroczysto¶ci±, ale bez LZW), PNG, JPEG, TIFF
oraz PostScript.

%prep
%setup -qn img%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE README changes license.terms
%{_libdir}/Img*
